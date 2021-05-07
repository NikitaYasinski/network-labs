import { Group, Student } from '@/models';
import { Teacher } from '@/models/teacher';
import { Faculty } from '@/models/faculty';
import { RowType } from '@/components/pages/Home/types';
import { ItemType } from '@/shared/types';

export const adaptRowData: Type = rawData =>
  // eslint-disable-next-line implicit-arrow-linebreak
  rawData.map((item: ItemType) => ({
    id: item.id,
    selected: false,
    cells: Object.entries(item)
      .filter(objectEntry => objectEntry[0] !== 'id')
      .map(objectEntry => ({ type: objectEntry[0], value: objectEntry[1] })),
  })) as RowType[];

type Type = (rawData: Student[] | Teacher[] | Group[] | Faculty[]) => RowType[];
